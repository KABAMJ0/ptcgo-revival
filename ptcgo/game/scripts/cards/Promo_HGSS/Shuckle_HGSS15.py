from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="01fdbb24-a700-5cf7-8b8e-735d5a8a81c3",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle", "Basic", "Shuckle"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=213,
    abilities=[
        Ability(
            title="Fermenting Liquid",
            game_text="Whenever you attach an Energy card from your hand to Shuckle, draw a card.",
            effect=unimplemented,
        ),
        Attack(
            title="Shell Stunner",
            game_text="Flip a coin. If heads, prevent all damage done to Shuckle by attacks during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)