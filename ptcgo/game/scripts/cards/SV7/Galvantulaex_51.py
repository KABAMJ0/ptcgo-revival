from ptcgo.game.card_effects.attacks_common import lock_opponent_plays, self_energy_discard_attack, bonus_if, defender_is_ex_or_v
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="52c183a9-afbc-5a22-961c-c1bd5e6118d3",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantulaex.Name",
    display_name="Galvantula ex",
    searchable_by=["Galvantula ex", "Stage 1", "Tera", "ex", "Galvantulaex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=51,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    abilities=[
        Attack(
            title="Charged Web",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex or Pok\u00e9mon V, this attack does 110 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            damage_operator="+",
            effect=bonus_if(defender_is_ex_or_v, 110),
        ),
        Attack(
            title="Fulgurite",
            game_text="Discard all Energy from this Pok\u00e9mon. During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=180,
            effect=self_energy_discard_attack(all_energy=True, also=lock_opponent_plays("item", damage=0)),
        ),
    ],
)