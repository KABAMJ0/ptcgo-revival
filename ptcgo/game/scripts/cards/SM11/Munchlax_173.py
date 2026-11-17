from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="49f282e1-1a33-5000-8990-d21c0281fa17",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munchlax.Name",
    display_name="Munchlax",
    searchable_by=["Munchlax", "Basic", "Munchlax"],
    subtypes=["Basic"],
    collector_number=173,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=446,
    abilities=[
        Ability(
            title="Snack Search",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, put a card from your discard pile on top of your deck. If you use this Ability, your turn ends.",
            effect=unimplemented,
        ),
    ],
)