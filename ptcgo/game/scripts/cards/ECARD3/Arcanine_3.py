from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="609ca60a-cab2-5320-8c32-b59a3b65edbf",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Ability(
            title="Energy Recharge",
            game_text="When you play Arcanine from your hand to evolve your Active Pok\u00e9mon, you may flip 3 coins. For each heads, choose a basic Energy card from your discard pile and attach it to Arcanine.",
            effect=unimplemented,
        ),
        Attack(
            title="Shake",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon, if any.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=gust_attack(damage_to_new_active=0, opponent_chooses=True),
        ),
        Attack(
            title="White Flames",
            game_text="Discard all Fire Energy cards attached to Arcanine.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=self_energy_discard_attack(all_energy=True,
                                             energy_type=PokemonTypes.FIRE,
                                             then_damage=70),
        ),
    ],
)