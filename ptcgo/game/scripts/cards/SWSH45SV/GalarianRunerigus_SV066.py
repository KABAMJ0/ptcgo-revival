from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c5da2874-307b-5db5-8a7b-26a532df2f21",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianRunerigus.Name",
    display_name="Galarian Runerigus",
    searchable_by=["Galarian Runerigus", "Stage 1", "GalarianRunerigus"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianYamask.Name",
    family_id=562,
    abilities=[
        Attack(
            title="Spreading Spite",
            game_text="For each damage counter on this Galarian Runerigus, put 2 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Mad Hammer",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=recoil_attack(30),
        ),
    ],
)