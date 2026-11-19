from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def sacred_fire_rider(ctx):
    """Heads: 80 to a chosen opposing Pokemon, ignoring Weakness/Resistance."""
    targets = list(ctx.opponent_pokemon_in_play())
    if not targets:
        return
    pick = await ctx.choose_pokemon(targets, "Choose a Pok\u00e9mon to take 80")
    if pick is not None:
        await ctx.deal_damage(80, target=pick, apply_modifiers=False)

card = PokemonCardDef(
    guid="3bd65ec4-ebae-54ae-be57-d83d10852b18",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name",
    display_name="Ho-Oh",
    searchable_by=["Ho-Oh", "Basic", "HoOh"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Sacred Fire",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Pok\u00e9mon. This attack does 80 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            effect=flip_gate(sacred_fire_rider),
        ),
    ],
)