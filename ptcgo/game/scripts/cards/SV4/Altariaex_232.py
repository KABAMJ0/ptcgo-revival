from ptcgo.game.card_effects.support_common import heal_targets
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bd3f1a92-d037-5128-a68d-9e8c8240cf92",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altariaex.Name",
    display_name="Altaria ex",
    searchable_by=["Altaria ex", "Stage 1", "ex", "Altariaex"],
    subtypes=["Stage 1", "ex"],
    collector_number=232,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Ability(
            title="Humming Heal",
            game_text="Once during your turn, you may heal 20 damage from each of your Pok\u00e9mon.",
            effect=heal_targets(20, scope="each_own"),
        ),
        Attack(
            title="Light Pulse",
            game_text="During your opponent's next turn, prevent all effects of attacks used by your opponent's Pok\u00e9mon done to this Pok\u00e9mon. (Damage is not an effect.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=140,
            effect=protect_next_turn(effects_too=True),
        ),
    ],
)