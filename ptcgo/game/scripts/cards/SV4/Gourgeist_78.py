from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37739065-a052-53cc-ab3e-a91329c92af7",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gourgeist.Name",
    display_name="Gourgeist",
    searchable_by=["Gourgeist", "Stage 1", "Gourgeist"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    family_id=710,
    abilities=[
        Ability(
            title="Startling Pumpkin",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, discard 2 random cards from your opponent's hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Shadow Bind",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)