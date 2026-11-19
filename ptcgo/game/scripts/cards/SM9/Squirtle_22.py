from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive

class _FloatingShell(Passive):
    """\"If you have a Stadium card in play, this Pokemon has no Retreat Cost.\" """

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        stadium = board.find_global_area("activeStadium")
        return 0 if stadium is not None and stadium.children else cost

card = PokemonCardDef(
    guid="459e0540-fbe5-5e35-a287-95ceb797cca4",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    display_name="Squirtle",
    searchable_by=["Squirtle", "Basic", "Squirtle"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=7,
    abilities=[
        Ability(
title="Floating Shell",
            game_text="If you have a Stadium card in play, this Pok\u00e9mon has no Retreat Cost.",
            passive=_FloatingShell(),
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)