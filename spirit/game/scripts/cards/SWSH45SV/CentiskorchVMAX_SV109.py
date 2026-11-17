from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="783da86a-47f4-5555-afba-aa10b780cccf",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CentiskorchVMAX.Name",
    display_name="Centiskorch VMAX",
    searchable_by=["Centiskorch VMAX", "VMAX", "CentiskorchVMAX"],
    subtypes=["VMAX"],
    collector_number=109,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CentiskorchV.Name",
    family_id=851,
    abilities=[
        Attack(
            title="G-Max Centiferno",
            game_text="This attack does 40 more damage for each Fire Energy attached to this Pok\u00e9mon. If you did any damage with this attack, you may attach a Fire Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)