from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="7799b003-3cfc-56cc-9382-41616e2da6ac",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ceruledgeex.Name",
    display_name="Ceruledge ex",
    searchable_by=["Ceruledge ex", "Stage 1", "Tera", "ex", "Ceruledgeex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=147,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=937,
    abilities=[
        Attack(
            title="Abyssal Flames",
            game_text="This attack does 20 more damage for each Energy card in your discard pile.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Raging Amethyst",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            damage=280,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)