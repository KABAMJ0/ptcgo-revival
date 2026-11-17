from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7291fc7a-ad8e-5faf-bcf2-f39260678536",
    key="COL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="COL1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=384,
    abilities=[
        Attack(
            title="Inferno Spear",
            game_text="Discard a Fire Energy and a Lightning Energy attached to Rayquaza.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)