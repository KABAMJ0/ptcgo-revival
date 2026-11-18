from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b21e5823-989e-5d90-922d-806dc96cb7a4",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arboliva.Name",
    display_name="Arboliva",
    searchable_by=["Arboliva", "Stage 2", "Arboliva"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    family_id=928,
    abilities=[
        Ability(
            title="Slippery Oil",
            game_text="Once during your turn, you may use this Ability. Switch out your opponent's Active Pok\u00e9mon to the Bench. (Your opponent chooses the new Active Pok\u00e9mon.)",
            effect=unimplemented,
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=heal_attack(30),
        ),
    ],
)