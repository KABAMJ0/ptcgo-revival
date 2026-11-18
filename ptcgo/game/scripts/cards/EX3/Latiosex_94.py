from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="38f39a28-dc01-570d-aba1-d6db7fe3a901",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latiosex.Name",
    display_name="Latios ex",
    searchable_by=["Latios ex", "Basic", "ex", "Latiosex"],
    subtypes=["Basic", "ex"],
    collector_number=94,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    family_id=381,
    abilities=[
        Attack(
            title="Energy Stream",
            game_text="Flip a coin. If heads, search your discard pile for a basic Energy card and attach it to Latios ex.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Luster Purge",
            game_text="Discard 3 Energy attached to Latios ex.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)