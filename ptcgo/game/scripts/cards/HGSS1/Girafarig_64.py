from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="13dfb921-f553-5ae5-a928-ad2272c5c197",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    display_name="Girafarig",
    searchable_by=["Girafarig", "Basic", "Girafarig"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="HGSS1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=203,
    abilities=[
        Attack(
            title="Show Off",
            game_text="Search your deck for up to 2 basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_basic_energy_card, count=2, reveal=True),
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)