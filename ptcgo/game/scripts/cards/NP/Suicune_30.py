from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import Triggers

async def pure_body(ctx):
    if ctx.source is None or getattr(ctx, "energy_receiver", None) is not ctx.source:
        return
    energy = getattr(ctx, "attached_energy", None)
    if energy is None or not energy_provides_type(energy, PokemonTypes.WATER.value):
        return
    await ctx.discard_energy_from(
        ctx.source, 1, prompt="Discard an Energy card attached to Suicune")

card = PokemonCardDef(
    guid="1ae739ea-f3f1-5cad-9ccb-9a0633b58eb2",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Ability(
            title="Pure Body",
            game_text="Whenever you attach a Water Energy card from your hand to Suicune, discard an Energy card attached to Suicune. (You can't attach a Water Energy card from your hand if Suicune has no Energy cards attached.)",
            effect=pure_body,
            trigger=Triggers.ON_ENERGY_ATTACHED,
        ),
        Attack(
            title="Hypno Wave",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 20 more damage. If tails, this attack does 30 damage and the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)