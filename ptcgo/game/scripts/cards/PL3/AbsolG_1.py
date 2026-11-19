from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7f1b95da-e651-5e0d-b15a-f2bd1e5eb02f",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AbsolG.Name",
    display_name="Absol G",
    searchable_by=["Absol G", "Basic", "SP", "AbsolG"],
    subtypes=["Basic", "SP"],
    collector_number=1,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=359,
    abilities=[
        Attack(
            title="Feint Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on that Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=snipe_attack(20, pool="any", apply_modifiers=False),
        ),
        Attack(
            title="Doom News",
            game_text="Return all Energy cards attached to Absol G to your hand. The Defending Pok\u00e9mon is Knocked Out at the end of your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)