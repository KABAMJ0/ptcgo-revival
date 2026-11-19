from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.support_common import gust_then

async def poison_new_defender(ctx, pokemon):
    await ctx.apply_special_condition(pokemon, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="1d1dcf44-e942-5c93-ba4d-a88a362bb4b1",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    display_name="Roselia",
    searchable_by=["Roselia", "Basic", "Roselia"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=315,
    abilities=[
        Ability(
            title="Reactive Aroma",
            game_text="As long as Roselia has any React Energy cards attached to it, remove 1 damage counter from each of your Pok\u00e9mon (excluding Pok\u00e9mon-ex) that has any React Energy cards attached to it between turns. You can't use more than 1 Reactive Aroma Pok\u00e9-Body each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Flick Poison",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch. The new Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_then(poison_new_defender, opponent_chooses=True),
        ),
    ],
)