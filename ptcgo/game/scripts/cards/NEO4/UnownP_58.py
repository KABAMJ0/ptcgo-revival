from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import Passive, carrier_pokemon


class _Perform(Passive):
    """Hidden Power deals again as much as Unown [P] took last turn."""

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if not (calc.is_attack and calc.is_opposing and attacker is not None):
            return
        if carrier_pokemon(carrier) is not attacker:
            return
        if (calc.attack_title or "") != "Hidden Power":
            return
        state = getattr(calc.board, "turn_state", None)
        taken = (getattr(state, "damage_taken_last_turn", None) or {}).get(
            attacker.entity_id, 0)
        if taken:
            calc.amount += taken


card = PokemonCardDef(
    guid="66fc955e-67e1-5aa5-af7a-08f72b239231",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownP.Name",
    display_name="Unown [P]",
    searchable_by=["Unown [P]", "Basic", "UnownP"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Perform]",
            game_text="If an attack damaged Unown [P] during your opponent's last turn and Unown [P] was your Active Pok\u00e9mon, Unown [P]'s Hidden Power attack does that much more damage to the Defending Pok\u00e9mon. This power can be used even if Unown [P] is Confused.",
            passive=_Perform(),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)