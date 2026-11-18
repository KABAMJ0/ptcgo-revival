from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="86d1e012-abec-5e06-b1ea-5c93dd81dc04",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosTadbulb.Name",
    display_name="Iono's Tadbulb",
    searchable_by=["Iono's Tadbulb", "Basic", "IonosTadbulb"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SV9",
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