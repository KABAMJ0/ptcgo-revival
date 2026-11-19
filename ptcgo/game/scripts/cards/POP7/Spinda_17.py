from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.trainers import is_basic_energy_card


def _shares_a_basic_type(holder, defender, energies) -> bool:
    held = set()
    for energy in energies(holder):
        if is_basic_energy_card(energy):
            held.update(type_value for type_value in range(1, 12)
                        if energy_provides_type(energy, type_value))
    if not held:
        return False
    for energy in energies(defender):
        if any(energy_provides_type(energy, type_value) for type_value in held):
            return True
    return False

async def synchro_punch(ctx):
    """10, plus 30 when a basic Energy on Spinda shares a type with one on the
    Defending Pokemon."""
    defender = ctx.defender
    if defender is None:
        await ctx.deal_damage(10)
        return
    bonus = _shares_a_basic_type(ctx.attacker, defender,
                                 lambda pokemon: ctx.attached_energies(pokemon))
    await ctx.deal_damage(40 if bonus else 10)

card = PokemonCardDef(
    guid="8c089fcb-8650-5d0d-8879-f22b9c4a8e82",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinda.Name",
    display_name="Spinda",
    searchable_by=["Spinda", "Basic", "Spinda"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="POP7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=327,
    abilities=[
        Attack(
            title="Dish Out",
            game_text="Draw a card from the top and the bottom of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Synchro Punch",
            game_text="If any basic Energy card attached to Spinda is the same type as any Energy attached to the Defending Pok\u00e9mon, this attack does 10 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=synchro_punch,
        ),
    ],
)