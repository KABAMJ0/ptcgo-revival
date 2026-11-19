from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack, recoil_attack

card = PokemonCardDef(
    guid="e4edb72a-59c1-569f-9a6e-93755935610e",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysBraviary.Name",
    display_name="Larry's Braviary",
    searchable_by=["Larry's Braviary", "Stage 1", "LarrysBraviary"],
    subtypes=["Stage 1"],
    collector_number=174,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysRufflet.Name",
    family_id=627,
    abilities=[
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Brave Bird",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=recoil_attack(30),
        ),
    ],
)