from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2fac3520-9426-56a0-bdcd-73b73d2077bc",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownW.Name",
    display_name="Unown [W]",
    searchable_by=["Unown [W]", "Basic", "UnownW"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Want]",
            game_text="Once during your turn (before your attack), if you have Unown [W], Unown [A], Unown [N], and Unown [T] on your Bench, you may flip a coin. If heads, put a Trainer card from your discard pile into your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)