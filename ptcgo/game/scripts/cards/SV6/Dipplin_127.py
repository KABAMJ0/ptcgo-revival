from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="0c4bd656-8960-5360-898e-96ddbf563d32",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dipplin.Name",
    display_name="Dipplin",
    searchable_by=["Dipplin", "Stage 1", "Dipplin"],
    subtypes=["Stage 1"],
    collector_number=127,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Syrup Catcher",
            game_text="Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot. This attack does 70 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            effect=gust_attack(damage_to_new_active=70),
        ),
    ],
)