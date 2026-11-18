from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e14b3ee2-3c62-5cfc-b6ed-663d292fb30f",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chingling.Name",
    display_name="Chingling",
    searchable_by=["Chingling", "Basic", "Chingling"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=433,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Chimecho from your hand onto Chingling (this counts as evolving Chingling) and remove all damage counters from Chingling.",
            effect=unimplemented,
        ),
        Attack(
            title="Uproar",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={},
            effect=unimplemented,
        ),
    ],
)