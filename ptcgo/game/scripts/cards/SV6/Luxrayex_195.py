from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="cfe7841e-0b04-5dc3-9857-2f163418e48a",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxrayex.Name",
    display_name="Luxray ex",
    searchable_by=["Luxray ex", "Stage 2", "ex", "Luxrayex"],
    subtypes=["Stage 2", "ex"],
    collector_number=195,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Attack(
            title="Piercing Gaze",
            game_text="Your opponent reveals their hand. Discard a card you find there.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=self_energy_discard_attack(all_energy=True),
        ),
        Attack(
            title="Volt Strike",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=250,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)