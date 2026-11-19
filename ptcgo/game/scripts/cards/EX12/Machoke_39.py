from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_gate


card = PokemonCardDef(
    guid="76ef0b3e-4f37-5397-b9f0-c43f6a1423c3",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    display_name="Machoke",
    searchable_by=["Machoke", "Stage 1", "Machoke"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Paranoid",
            game_text="As long as Machoke is Confused, Machoke's attacks do 50 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Split Kick",
            game_text="Does 20 damage to each Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=flip_gate(discard_opponent_energy_attack(1)),
        ),
        Attack(
            title="Magnum Punch",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)