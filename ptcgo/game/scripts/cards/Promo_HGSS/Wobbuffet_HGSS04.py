from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.session.passives import Passive, carrier_pokemon


from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

class TenaciousBindPassive(Passive):
    """While Wobbuffet is Active, the opponent's Active pays [C][C] more."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if holder is None or not is_in_active_spot(holder):
            return cost
        if pokemon is None or pokemon.owning_player_id == holder.owning_player_id:
            return cost
        if not is_in_active_spot(pokemon):
            return cost
        return cost + 2


card = PokemonCardDef(
    guid="6264ff49-dd7a-5586-be31-a3cbd371954c",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Wobbuffet"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Ability(
            title="Tenacious Bind",
            game_text="As long as Wobbuffet is your Active Pok\u00e9mon, your opponent's Active Pok\u00e9mon's Retreat Cost is ColorlessColorless more.",
            passive=TenaciousBindPassive(),
        ),
        Attack(
            title="Trip Over",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 30 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(50)),
        ),
    ],
)