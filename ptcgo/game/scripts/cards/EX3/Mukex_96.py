from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="94b3e0ca-eb84-576d-87b6-465aaa54c51b",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mukex.Name",
    display_name="Muk ex",
    searchable_by=["Muk ex", "Stage 1", "ex", "Mukex"],
    subtypes=["Stage 1", "ex"],
    collector_number=96,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Toxic Gas",
            game_text="As long as Muk ex is your Active Pok\u00e9mon, ignore all Pok\u00e9-Powers and Pok\u00e9-Bodies other than Toxic Gas.",
            effect=unimplemented,
        ),
        Attack(
            title="Poison Breath",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Slimy Water",
            game_text="Does 40 damage plus 10 more damage for each Colorless Energy in the Defending Pok\u00e9mon's Retreat Cost (after applying effects to the Retreat Cost).",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)