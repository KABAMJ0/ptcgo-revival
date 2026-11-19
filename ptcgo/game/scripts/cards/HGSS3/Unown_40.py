from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _is_darkness(card) -> bool:
    return energy_provides_type(card, PokemonTypes.DARKNESS.value)

card = PokemonCardDef(
    guid="000a0a92-e455-5f06-913a-f39ccd4520bf",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown",
    searchable_by=["Unown", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="HGSS3",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="DARK",
            game_text="Once during your turn, when you put Unown from your hand onto your Bench, you may search your deck for a Darkness Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            trigger=Triggers.ON_PLAY,
            effect=search_to_hand(_is_darkness, count=1, reveal=True),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
