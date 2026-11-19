from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class _WimpOutPassive(Passive):
    """"During your first turn, this Pokemon has no Retreat Cost."

    Turn 1 and turn 2 of `turn_number` ARE each player's first turn (the
    counter advances once per player turn), so the pair covers the owner's."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        state = getattr(board, "turn_state", None)
        if carrier_pokemon(carrier) is not pokemon or state is None \
                or state.turn_number > 2:
            return cost
        return 0



card = PokemonCardDef(
    guid="1fbf863b-a548-5f10-8842-9db1e4b33afc",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    display_name="Wimpod",
    searchable_by=["Wimpod", "Basic", "Wimpod"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=767,
    abilities=[
        Ability(
            title="Wimp Out",
            game_text="During your first turn, this Pok\u00e9mon has no Retreat Cost.",
            passive=_WimpOutPassive(),
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)