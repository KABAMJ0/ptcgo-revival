from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.session.passives import Passive, carrier_pokemon


class ConductiveBodyPassive(Passive):
    """While Beldum is your Active Pokemon, its retreat cost is 1 less for each
    Beldum on your Bench."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if holder is None or pokemon is not holder or not is_in_active_spot(holder):
            return cost
        bench = board.find_player_area(holder.owning_player_id, "bench")
        others = sum(
            1 for benched in (bench.children if bench else [])
            if benched.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Beldum"
        )
        return max(0, cost - others)


card = PokemonCardDef(
    guid="1d2b4707-3001-50ee-8e15-9f9cc459d7a8",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum δ",
    searchable_by=["Beldum \u03b4", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=374,
    abilities=[
        Ability(
            title="Conductive Body",
            game_text="As long as Beldum is your Active Pok\u00e9mon, you pay Colorless less to retreat Beldum for each Beldum on your Bench.",
            passive=ConductiveBodyPassive(),
        ),
        Attack(
            title="Take Down",
            game_text="Beldum does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)