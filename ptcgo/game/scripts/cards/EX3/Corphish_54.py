from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="a55ffa92-2bf2-5282-af99-c6afbdbc6d1b",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    display_name="Corphish",
    searchable_by=["Corphish", "Basic", "Corphish"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="EX3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=341,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Toxic Grip",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)