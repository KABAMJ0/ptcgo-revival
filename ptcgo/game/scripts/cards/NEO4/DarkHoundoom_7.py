from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def _dark_fire(ctx):
    """Dark Fire: 30, or 50 with a Darkness Energy discarded to feed it."""
    darkness = [e for e in ctx.attached_energies(ctx.attacker)
                if energy_provides_type(e, PokemonTypes.DARKNESS.value)]
    if darkness:
        await ctx.discard_cards(darkness[:1])
        await ctx.deal_damage(50)
    else:
        await ctx.deal_damage(30)

card = PokemonCardDef(
    guid="eff360fd-70bb-5753-97a6-05f0e689266f",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkHoundoom.Name",
    display_name="Dark Houndoom",
    searchable_by=["Dark Houndoom", "Stage 1", "DarkHoundoom"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Eerie Howl",
            game_text="If your opponent's Bench isn't full, look at his or her hand. If your opponent has any Baby Pok\u00e9mon or Basic Pok\u00e9mon there, choose 1 of them and put it on his or her Bench. Then, switch it with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dark Fire",
            game_text="If there are any Darkness Energy cards attached to Dark Houndoom, discard 1 of them and this attack does 30 damage plus 20 more damage (plus 10 more damage for the Darkness Energy you discarded). If there aren't any, this attack does 30 damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=_dark_fire,
        ),
    ],
)