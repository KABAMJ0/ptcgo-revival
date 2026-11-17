from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a9f8135a-699d-5e24-a939-0ee27fc8c9eb",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    display_name="Luxio",
    searchable_by=["Luxio", "Stage 1", "Luxio"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    family_id=403,
    abilities=[
        Ability(
            title="Fighting Roar",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex, this Pok\u00e9mon can evolve during your first turn or the turn you play it.",
            effect=unimplemented,
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)