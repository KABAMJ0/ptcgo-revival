from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="147b11ad-52cb-5dc7-a59a-16d59749d266",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios",
    searchable_by=["Latios", "Basic", "Latios"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    family_id=381,
    abilities=[
        Ability(
            title="Luster Float",
            game_text="If you have Latias in play, the Retreat Cost for Latios is 0.",
            effect=unimplemented,
        ),
        Attack(
            title="Infinite Wing",
            game_text="Discard 2 Energy attached to Latios.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            effect=unimplemented,
        ),
    ],
)