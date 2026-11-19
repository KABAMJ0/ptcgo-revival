from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per


card = PokemonCardDef(
    guid="9fdb84c6-6d45-5362-8898-6ad65efa6a03",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocGX.Name",
    display_name="Lycanroc-GX",
    searchable_by=["Lycanroc-GX", "Stage 1", "GX", "LycanrocGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=66,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=744,
    abilities=[
        Ability(
            title="Bloodthirsty Eyes",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
        Attack(
            title="Dangerous Rogue-GX",
            game_text="This attack does 50 damage for each of your opponent's Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_bench('opponent'), 50),
        ),
    ],
)