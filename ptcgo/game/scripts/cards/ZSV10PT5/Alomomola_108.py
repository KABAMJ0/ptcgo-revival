from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.content.definitions import Activations
from ptcgo.game.card_effects.passives_common import is_in_active_spot

import json

from ptcgo.game.card_effects.trainers import bench_named_pokemon
from ptcgo.game.content.definitions import def_for
from ptcgo.game.session.effects import is_basic_pokemon


def _printed_hp(card):
    definition = def_for(card.archetype_id)
    spec = (getattr(definition, "extra_attributes", {}) or {}).get(
        str(AttrID.HP.value))
    value = spec.get("value") if isinstance(spec, dict) else spec
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def _small_basic(card):
    return is_basic_pokemon(card) and 0 < _printed_hp(card) <= 70


gentle_fin = bench_named_pokemon(_small_basic, source="discard",
                                 label="Basic Pok\u00e9mon with 70 HP or less")


def _gentle_fin_offered(board, player_id, pokemon):
    if not is_in_active_spot(pokemon):
        return False
    area = board.find_player_area(player_id, "discard")
    bench = board.find_player_area(player_id, "bench")
    if bench is not None and len(bench.children) >= 5:
        return False
    return any(_small_basic(card) for card in (area.children if area else []))


card = PokemonCardDef(
    guid="63e76787-7e48-59bc-b9ee-ffe9313ddd18",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alomomola.Name",
    display_name="Alomomola",
    searchable_by=["Alomomola", "Basic", "Alomomola"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=594,
    abilities=[
        Ability(
            title="Gentle Fin",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may put a Basic Pok\u00e9mon with 70 HP or less from your discard pile onto your Bench.",
            effect=gentle_fin,
            activation=Activations.ONCE_PER_TURN,
            condition=_gentle_fin_offered,
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)