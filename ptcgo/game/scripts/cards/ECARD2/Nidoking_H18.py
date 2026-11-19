from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_gate, spread_damage
from ptcgo.game.card_effects.passives_common import is_in_active_spot, unafflicted
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_DAMAGE_COUNTER = 10  # one damage counter, the unit the card prints


def _earth_rage_ready(board, player_id, pokemon) -> bool:
    return is_in_active_spot(pokemon) and unafflicted(board, player_id, pokemon)

card = PokemonCardDef(
    guid="18fede1e-28eb-5344-8bb9-d4853dcab8cf",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Ability(
            title="Earth Rage",
            game_text="Once during your turn (before your attack), if Nidoking is your Active Pok\u00e9mon, you may flip a coin. If heads, put a damage counter on each of your opponent's Benched Pok\u00e9mon. This power can't be used if Nidoking is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_earth_rage_ready,
            effect=flip_gate(then=spread_damage(_DAMAGE_COUNTER, side="opponent")),
        ),
        Attack(
            title="Giant Horn",
            game_text="Flip a coin. If heads, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(80)),
        ),
    ],
)
