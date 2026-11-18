from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9d2bbe40-28d9-565f-a183-c21c970371b2",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKoko.Name",
    display_name="Tapu Koko ◇",
    searchable_by=["Tapu Koko \u25c7", "Basic", "Prism Star", "TapuKoko"],
    subtypes=["Basic", "Prism Star"],
    collector_number=51,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=785,
    abilities=[
        Ability(
            title="Dance of the Ancients",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may choose 2 of your Benched Pok\u00e9mon and attach a Lightning Energy card from your discard pile to each of them. If you do, discard all cards from this Pok\u00e9mon and put it in the Lost Zone.",
            effect=unimplemented,
        ),
        Attack(
            title="Mach Bolt",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)