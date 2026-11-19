from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.passives_common import (
    is_in_active_spot,
    no_weakness_passive,
)
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.card_effects.support_common import attach_from_discard

def _is_basic_energy(card) -> bool:
    return (is_energy_card(card)
            and not card.get_attribute(AttrID.IS_SPECIAL_ENERGY))


def _is_benched(pokemon) -> bool:
    return not is_in_active_spot(pokemon)

card = PokemonCardDef(
    guid="75a5d6de-2178-5225-b76a-3ec79a0b0272",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArcanineBREAK.Name",
    display_name="Arcanine BREAK",
    searchable_by=["Arcanine BREAK", "BREAK", "ArcanineBREAK"],
    subtypes=["BREAK"],
    collector_number=180,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    family_id=59,
    abilities=[
        Attack(
            title="Turbo Flame",
            game_text="Attach 2 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=attach_from_discard(_is_basic_energy, count=2, target=_is_benched),
        ),
    ],
)