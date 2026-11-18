from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="72022a30-9066-5160-b6dc-4fb7ca311bec",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownG.Name",
    display_name="Unown [G]",
    searchable_by=["Unown [G]", "Basic", "UnownG"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="GUARD",
            game_text="Once during your turn (before your attack), if Unown G is on your Bench, you may discard all cards attached to Unown G and attach Unown G to 1 of your Pok\u00e9mon as a Pok\u00e9mon Tool card. As long as Unown G is attached to a Pok\u00e9mon, prevent all effects of attacks, excluding damage, done to that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="If Unown G has any damage counters on it, this attack's base damage is 10.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)