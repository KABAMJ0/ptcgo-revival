from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="e3173320-d2e5-58fe-941d-5551e9600aa0",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasOddish.Name",
    display_name="Erika's Oddish",
    searchable_by=["Erika's Oddish", "Basic", "ErikasOddish"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=43,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)