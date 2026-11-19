from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, snipe_attack


async def _called_shot(ctx):
    """10 damage per Grass Energy on Exeggutor to one of their Benched Pokemon,
    with no Weakness or Resistance (it is bench damage)."""
    amount = 10 * count_energy("self", PokemonTypes.GRASS)(ctx)
    await snipe_attack(amount, pool="bench", count=1, apply_modifiers=False)(ctx)


card = PokemonCardDef(
    guid="3ea27f84-0a24-5353-885e-3fa46b61f53d",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor",
    searchable_by=["Exeggutor", "Stage 1", "Exeggutor"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Super Eggsplosion",
            game_text="Discard any number of Energy cards attached to any of your Pok\u00e9mon. Flip a number of coins equal to the number of Energy cards discarded this way. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Called Shot",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage times the amount of Grass Energy attached to Exeggutor. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=_called_shot,
        ),
    ],
)