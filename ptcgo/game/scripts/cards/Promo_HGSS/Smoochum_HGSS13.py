from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.session.passives import Passive, carrier_pokemon


class AsleepShieldPassive(Passive):
    """While the holder is Asleep, attacks do it no damage at all."""

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing) or holder is None:
            return False
        if calc.target is not holder:
            return False
        conditions = holder.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        return "asleep" in {str(label).lower() for label in conditions}


async def energy_antics(ctx):
    """Move an Energy between the opponent's Pokemon, then Smoochum Asleep."""
    sources = [p for p in ctx.opponent_pokemon_in_play() if ctx.attached_energies(p)]
    if not sources:
        return
    holder = sources[0] if len(sources) == 1 else await ctx.choose_pokemon(
        sources, "Choose a Pokemon to move an Energy from")
    if holder is None:
        return
    energies = list(ctx.attached_energies(holder))
    picked = energies[:1] if len(energies) == 1 else await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose an Energy to move")
    destinations = [p for p in ctx.opponent_pokemon_in_play() if p is not holder]
    if picked and destinations:
        target = destinations[0] if len(destinations) == 1 else await ctx.choose_pokemon(
            destinations, "Choose a Pokemon to move the Energy to")
        if target is not None:
            ctx.board.attach_card(picked[0].entity_id, target.entity_id)
    if ctx.attacker is not None:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
from ptcgo.game.attributes import AttrID
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

class AsleepShieldPassive(Passive):
    """While the holder is Asleep, attacks do it no damage at all."""

    def prevents_damage(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing) or holder is None:
            return False
        if calc.target is not holder:
            return False
        conditions = holder.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        labels = {str(label).lower() for label in conditions}
        return "asleep" in labels


card = PokemonCardDef(
    guid="82535574-9cf4-5102-a22b-50359067e382",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoochum.Name",
    display_name="Smoochum",
    searchable_by=["Smoochum", "Basic", "Smoochum"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=238,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Smoochum is Asleep, prevent all damage done to Smoochum by attacks.",
            passive=AsleepShieldPassive(),
        ),
        Attack(
            title="Energy Antics",
            game_text="Move an Energy card attached to 1 of your opponent's Pok\u00e9mon to another of your opponent's Pok\u00e9mon. Smoochum is now Asleep.",
            cost={},
            effect=energy_antics,
        ),
    ],
)