from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d5d412a7-6e03-518c-80d7-22945a96813f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosTadbulb.Name",
    display_name="Iono's Tadbulb",
    searchable_by=["Iono's Tadbulb", "Basic", "IonosTadbulb"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=938,
    abilities=[
        Attack(
            title="Tiny Charge",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)