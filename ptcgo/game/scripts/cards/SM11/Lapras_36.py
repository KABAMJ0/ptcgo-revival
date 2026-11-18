from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37096c4c-61f1-5470-8b6d-fedd139f1d95",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=131,
    abilities=[
        Ability(
            title="Mermaid's Call",
            game_text="Once during your turn (before your attack), you may put a Misty's Favor card from your discard pile into your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)