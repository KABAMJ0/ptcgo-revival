from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8cae8be2-24eb-537f-9b41-49bcb4c3df22",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chingling.Name",
    display_name="Chingling",
    searchable_by=["Chingling", "Basic", "Chingling"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="PL3",
    rarity=Rarities.Common,
    hp=50,
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
            title="Chime",
            game_text="Search your opponent's discard pile for a Supporter card and use the effect of that card as the effect of this attack. (The Supporter card remains in your opponent's discard pile.)",
            cost={},
            effect=unimplemented,
        ),
    ],
)