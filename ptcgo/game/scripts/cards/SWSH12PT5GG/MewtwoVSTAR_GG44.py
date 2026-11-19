from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from ptcgo.game.card_effects.pokemon import energy_provides_type

async def psy_purge(ctx):
    energies = [
        e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)
        if energy_provides_type(e, PokemonTypes.PSYCHIC.value)
    ]
    picks = await ctx.choose_cards(
        energies, 3, minimum=0,
        prompt="Discard up to 3 Psychic Energy from your Pokémon.",
    )
    await ctx.discard_cards(picks)
    if picks:
        await ctx.deal_damage(90 * len(picks))

card = PokemonCardDef(
    guid="30b8dc56-bcf5-5bac-9c00-28a90572b407",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoVSTAR.Name",
    display_name="Mewtwo VSTAR",
    searchable_by=["Mewtwo VSTAR", "VSTAR", "MewtwoVSTAR"],
    subtypes=["VSTAR"],
    collector_number=44,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloVSTAR,
    hp=280,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoV.Name",
    family_id=150,
    abilities=[
        Attack(
            title="Psy Purge",
            game_text="Discard up to 3 Psychic Energy from your Pok\u00e9mon. This attack does 90 damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="x",
            effect=psy_purge,
        ),
        Attack(
            title="Star Raid",
            game_text="This attack does 120 damage to each of your opponent's Pok\u00e9mon V. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)