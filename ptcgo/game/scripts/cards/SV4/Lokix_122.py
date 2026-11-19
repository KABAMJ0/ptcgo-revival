from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities
from ptcgo.game.card_effects.support_common import switch_self_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per, damage_counters_on
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cfe08784-d6e3-522f-86aa-ba4d2a6ec6e4",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lokix.Name",
    display_name="Lokix",
    searchable_by=["Lokix", "Stage 1", "Lokix"],
    subtypes=["Stage 1"],
    collector_number=122,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name",
    family_id=919,
    abilities=[
        Attack(
            title="Bounce",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=switch_self_attack(),
        ),
        Attack(
            title="Punishing Kick",
            game_text="This attack does 40 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 40, base=10),
        ),
    ],
)