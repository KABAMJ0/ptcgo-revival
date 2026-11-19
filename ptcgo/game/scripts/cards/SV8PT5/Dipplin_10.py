from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per
from ptcgo.game.session.passives import Passive

class FestivalLeadPassive(Passive):
    """While Festival Grounds is in play this Pokemon may attack twice: the
    first attack keeps the turn (the printed Knock Out sentence is the timing
    reminder, not a condition)."""

    def attack_keeps_turn(self, attacker, ability, ctx, carrier):
        if attacker is not carrier:
            return False
        stadium = ctx.stadium_in_play()
        if stadium is None:
            return False
        if def_for(stadium.archetype_id).display_name != "Festival Grounds":
            return False
        uses = [entry for entry in ctx.session.turn_state.attacks_used
                if entry[0] == carrier.entity_id]
        return len(uses) == 1

card = PokemonCardDef(
    guid="e0caecc8-6e6e-5d17-84d0-9edfb4f5719e",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dipplin.Name",
    display_name="Dipplin",
    searchable_by=["Dipplin", "Stage 1", "Dipplin"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Ability(
            title="Festival Lead",
            game_text="If Festival Grounds is in play, this Pok\u00e9mon may use an attack it has twice. If the first attack Knocks Out your opponent's Active Pok\u00e9mon, you may attack again after your opponent chooses a new Active Pok\u00e9mon.",
            passive=FestivalLeadPassive(),
        ),
        Attack(
            title="Do the Wave",
            game_text="This attack does 20 damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_bench("mine"), per=20, base=0),
        ),
    ],
)