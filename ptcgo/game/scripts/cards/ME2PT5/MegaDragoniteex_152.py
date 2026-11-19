from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="ea5b4a91-0c51-5f16-a8d4-bd044c1a175d",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDragoniteex.Name",
    display_name="Mega Dragonite ex",
    searchable_by=["Mega Dragonite ex", "Stage 2", "MEGA", "ex", "MegaDragoniteex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=152,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=370,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Sky Transport",
            game_text="Once during your turn, you may use this Ability. Switch your Active Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Ryuno Glide",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 2},
            damage=330,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)