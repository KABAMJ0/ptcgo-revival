from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="094f4273-088c-553b-a534-57a423fd4e2d",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompLVX.Name",
    display_name="Garchomp LV.X",
    searchable_by=["Garchomp LV.X", "Level-Up", "GarchompLVX"],
    subtypes=["Level-Up"],
    collector_number=97,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name",
    family_id=445,
    abilities=[
        Ability(
            title="Dragon Pulse",
            game_text="Once during your turn (before your attack), when you put Garchomp LV.X from your hand onto your Active Garchomp, you may flip 3 coins. For each heads, put 1 damage counter on each of your opponent's Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Restore",
            game_text="Search your discard pile for a Pok\u00e9mon (excluding Pok\u00e9mon LV.X) and put it onto your Bench as a Basic Pok\u00e9mon. Then, you may search your discard pile for up to 3 basic Energy cards and attach them to that Pok\u00e9mon.",
            cost={},
            effect=unimplemented,
        ),
    ],
)