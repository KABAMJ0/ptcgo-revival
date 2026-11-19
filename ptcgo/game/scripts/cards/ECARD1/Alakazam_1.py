from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import bonus_if, count_energy
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.data_utils import def_for


def _energy_counts_differ(ctx):
    return count_energy("self", cards=True)(ctx) != count_energy("defender", cards=True)(ctx)


async def _psymimic(ctx):
    candidates = []
    for pokemon in ctx.opponent_pokemon_in_play():
        for ability in getattr(def_for(pokemon.archetype_id), "abilities", []):
            if isinstance(ability, Attack):
                candidates.append((pokemon, ability))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    await ctx.use_attack(picked[1])


card = PokemonCardDef(
    guid="9f83b238-35a9-55c7-b157-e8fafab56d6e",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alakazam.Name",
    display_name="Alakazam",
    searchable_by=["Alakazam", "Stage 2", "Alakazam"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    family_id=63,
    abilities=[
        Ability(
            title="Psymimic",
            game_text="Once during your turn, instead of Alakazam's normal attack, you may choose 1 of your opponent's Pok\u00e9mon's attacks. Alakazam copies that attack including its Energy costs and anything else required in order to use that attack, such as discarding Energy cards. (No matter what type that Pok\u00e9mon is, Alakazam's type is still Psychic.) This power can't be used if Alakazam is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=unafflicted,
            effect=_psymimic,
        ),
        Attack(
            title="Syncroblast",
            game_text="If Alakazam and the Defending Pok\u00e9mon don't have the same number of Energy cards attached to them, this attack's base damage is 20 instead of 80.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=bonus_if(_energy_counts_differ, -60, base=80),
        ),
    ],
)