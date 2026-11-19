from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.session.passives import Passive, carrier_pokemon

class DarkHolePassive(Passive):
    """While the carrier is on the Bench, Darkness Weakness is not applied to any
    of its owner's Pokemon."""

    def modify_weakness(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or is_in_active_spot(holder):
            return
        if calc.target.owning_player_id != holder.owning_player_id:
            return
        weakness = calc.target.get_attribute(AttrID.WEAKNESS_TYPES) or []
        if PokemonTypes.DARKNESS.value in weakness:
            calc.weakness_applies = False

async def shadow_beam(ctx):
    """Put 2 damage counters on the Defending Pokemon for each Energy attached
    to Dusclops ex (one counter is 10 HP)."""
    counters = count_energy("self")(ctx) * 2
    if counters <= 0:
        return
    await ctx.deal_damage(counters * 10, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="2d372e66-30eb-5d1f-b074-99f84d2733eb",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclopsex.Name",
    display_name="Dusclops ex",
    searchable_by=["Dusclops ex", "Stage 1", "ex", "Dusclopsex"],
    subtypes=["Stage 1", "ex"],
    collector_number=94,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Dark Hole",
            game_text="As long as Dusclops ex is on your Bench, don't apply Darkness Weakness for all of your Pok\u00e9mon is play.",
            effect=None,
            passive=DarkHolePassive(),
        ),
        Attack(
            title="Shadow Beam",
            game_text="Put 2 damage counters on the Defending Pok\u00e9mon for each Energy attached to Dusclops ex.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=shadow_beam,
        ),
    ],
)