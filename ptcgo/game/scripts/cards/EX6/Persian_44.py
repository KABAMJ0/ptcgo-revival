from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="9c7b8073-b764-5147-8176-e281405d58e1",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name",
    display_name="Persian",
    searchable_by=["Persian", "Stage 1", "Persian"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=52,
    abilities=[
        Ability(
            title="Thick Skin",
            game_text="Persian can't be affected by any Special Conditions.",
            effect=unimplemented,
        ),
        Attack(
            title="Poison Claws",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Shining Claws",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)