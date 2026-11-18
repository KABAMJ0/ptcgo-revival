from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a5fa50a4-b584-595e-bf0d-6fac0b73fd36",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BuriedFossil.Name",
    display_name="Buried Fossil",
    searchable_by=["Buried Fossil", "Basic", "BuriedFossil"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    abilities=[
        Ability(
            title="Reconstruction",
            game_text="Once during your turn (before your attack), if you have a basic Energy card in your hand, you may search your deck for an Omanyte or Kabuto card, show it to your opponent, and put it into your hand. Then put a basic Energy card from your hand into your deck. Shuffle your deck afterward.",
            effect=unimplemented,
        ),
    ],
)