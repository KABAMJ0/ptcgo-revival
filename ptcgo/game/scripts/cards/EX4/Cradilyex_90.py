from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.passives_common import evolution_lock_passive
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="5da3fb05-cd3a-5fa0-b4bb-598d9dd765de",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cradilyex.Name",
    display_name="Cradily ex",
    searchable_by=["Cradily ex", "Stage 2", "ex", "Cradilyex"],
    subtypes=["Stage 2", "ex"],
    collector_number=90,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    family_id=346,
    abilities=[
        Ability(
            title="Primal Vibes",
            game_text="As long as Cradily ex is your Active Pok\u00e9mon, your opponent can't play a Pok\u00e9mon from his or her hand to evolve his or her Active Pok\u00e9mon.",
            passive=evolution_lock_passive(active_only=True),
        ),
        Attack(
            title="Eerie Light",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Acidic Poison",
            game_text="The Defending Pok\u00e9mon is now Poisoned and Burned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)