from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.passives_common import boost_own_next_turn
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="015ca17d-8340-5f21-b107-b8525e38c829",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=178,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Meteor Mash",
            game_text="During your next turn, this Pok\u00e9mon's Meteor Mash attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            damage=60,
            effect=boost_own_next_turn(60, attack_title="Meteor Mash"),
        ),
        Attack(
            title="Luster Blast",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=200,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)