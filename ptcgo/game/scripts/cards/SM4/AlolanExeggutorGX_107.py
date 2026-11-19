from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import (condition_attack, count_energy,
                                                    snipe_attack)

card = PokemonCardDef(
    guid="437c3481-74ed-59bb-a876-3fb37a0ca9ce",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutorGX.Name",
    display_name="Alolan Exeggutor-GX",
    searchable_by=["Alolan Exeggutor-GX", "Stage 1", "GX", "AlolanExeggutorGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=107,
    set_code="SM4",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Tropical Head",
            game_text="This attack does 20 damage times the amount of Energy attached to this Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=snipe_attack(lambda ctx: count_energy('self')(ctx) * 20, pool='any',
                                count=1, apply_modifiers=False),
        ),
        Attack(
            title="Dragon Hammer",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Tower-Go-Round-GX",
            game_text="Move any number of Energy from your Pok\u00e9mon to your other Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=unimplemented,
        ),
    ],
)